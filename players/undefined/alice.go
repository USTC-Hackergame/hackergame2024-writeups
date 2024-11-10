// write a web server that listens on port 8080
// on post request to / extract text body to a variable and print it
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
)

var body []byte

var file = "/space/file"

func main() {
	fmt.Println("Server started on port 8080")
	http.HandleFunc("/update/*", handler)
	http.HandleFunc("/exit", exitHandler)
	http.ListenAndServe(":8080", nil)
}

func exitHandler(w http.ResponseWriter, r *http.Request) {
	os.Exit(0)
}

func replaceFile(filepath string, content []byte, offset int) ([]byte, error) {
	// replace the content of the file at offset with the new content, return original content
	file, err := os.OpenFile(filepath, os.O_RDWR, 0644)
	if err != nil {
		return nil, err
	}
	bytes := make([]byte, len(content))
	file.ReadAt(bytes, int64(offset))
	file.Close()
	writer, err := os.OpenFile(filepath, os.O_WRONLY, 0644)
	if err != nil {
		return nil, err
	}
	writer.WriteAt(content, int64(offset))
	writer.Close()
	return bytes, nil
}

func handler(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		return
	}
	path := r.URL.Path
	offset, err := strconv.ParseInt(path[1:], 10, 64)
	if err != nil {
		return
	}
	fmt.Println("offset", offset)
	original, err := replaceFile(file, body, int(offset))
	if err != nil {
		return
	}
	// fmt.Println("original", string(original))
	// return original
	w.Write(original)
}
