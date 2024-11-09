for i = 0, 255 do
	if i % 8 == 0 then
		io.write "\n\t.byte "
	end

	io.write(("%d"):format(i == 0 and 4 or 0));

	if i % 8 ~= 7 then
		io.write ", "
	end
end

io.write '\n'
