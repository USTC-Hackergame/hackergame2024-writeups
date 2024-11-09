for i = 0, 255 do
	if i % 8 == 0 then
		io.write "\n\t.byte "
	end

	io.write(("0x%x"):format(0xff & (~i)));

	if i % 8 ~= 7 then
		io.write ", "
	end
end
io.write '\n'
