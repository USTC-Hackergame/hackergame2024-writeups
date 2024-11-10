int __fastcall main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+8h] [rbp-F8h]
  int j; // [rsp+Ch] [rbp-F4h]
  int k; // [rsp+10h] [rbp-F0h]
  int c; // [rsp+14h] [rbp-ECh]
  FILE *stream; // [rsp+18h] [rbp-E8h]
  int v9; // [rsp+24h] [rbp-DCh]
  int v10; // [rsp+28h] [rbp-D8h]
  int v11; // [rsp+2Ch] [rbp-D4h]
  _QWORD v12[4]; // [rsp+30h] [rbp-D0h] BYREF
  char s1[17]; // [rsp+50h] [rbp-B0h] BYREF
  char v14[17]; // [rsp+61h] [rbp-9Fh] BYREF
  char v15[134]; // [rsp+72h] [rbp-8Eh] BYREF
  unsigned __int64 v16; // [rsp+F8h] [rbp-8h]
  __int64 savedregs; // [rsp+100h] [rbp+0h] BYREF

  v16 = __readfsqword(0x28u);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  setvbuf(stderr, 0LL, 2, 0LL);
  for ( i = 0; i <= 2; ++i )
  {
    printf("Data %d:", (unsigned int)(i + 1));
    if ( (unsigned int)__isoc99_scanf("%16s", &s1[17 * i]) != 1 || (unsigned int)hex_to_bin(&s1[17 * i], &v12[i], 8LL) )
    {
      fwrite("Invalid input\n", 1uLL, 0xEuLL, stderr);
      return 1;
    }
  }
  if ( !strcmp(s1, v14) || !strcmp(s1, v15) || !strcmp(v14, v15) )
  {
    puts("Input should be different");
    return 1;
  }
  for ( j = 0; j <= 2; ++j )
  {
    SHA256(&v12[j], 8LL, &v15[32 * j + 30]);
    *(&v9 + j) = 0;
    for ( k = 0; k <= 3; ++k )
      *(&v9 + j) = *((unsigned __int8 *)&savedregs + 32 * j + k - 84) | (*(&v9 + j) << 8);
  }
  if ( v9 == v10 && v10 == v11 )
  {
    stream = fopen("flag1", "r");
    if ( !stream )
    {
      fwrite("Can't open file\n", 1uLL, 0x10uLL, stderr);
      return 1;
    }
    while ( 1 )
    {
      c = fgetc(stream);
      if ( c == -1 )
        break;
      putchar(c);
    }
    fclose(stream);
  }
  else
  {
    puts("Wrong answer");
  }
  return 0;
}
