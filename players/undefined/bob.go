package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
)

// read the content of file1 in chunk of 1kb

var filename = "/space/file"

func withOffset(offset int64) error {
	file, err := os.Open(filename)
	if err != nil {
		return err
	}
	content := make([]byte, 1024)
	file.ReadAt(content, int64(offset))
	file.Close()

	// post the body to localhost:8080
	resp, err := http.Post("http://127.0.0.1:8080/"+strconv.FormatInt(offset, 10), "text/plain", bytes.NewReader(content))
	if err != nil {
		return err
	}
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return err
	}
	file, err = os.OpenFile(filename, os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	fmt.Println("received", int64(offset))
	file.WriteAt(body, int64(offset))
	file.Close()
	defer resp.Body.Close()
	return nil
}

func main() {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println(err)
	}
	fi, err := file.Stat()
	if err != nil {
		fmt.Println(err)
	}
	size := fi.Size()
	fmt.Printf("The file is %d bytes long", size)
	for i := int64(0); i < size; i += 1024 {
		err = withOffset(i)
		if err != nil {
			fmt.Println(err)
		}
	}
	http.Post("http://127.0.0.1:8080/exit", "text/plain", nil)
}
