# This script is used to convert the multi-file project into a single C file because of compatibility
# issues with the copyright analysis tools my university uses. 
# 
# The script recursively searches a given root directory for all .c and .h files and appends them to a single output C file.
# This process takes into consideration the #include statements in the files.
# For example, if a file includes another file, the other file should be added first to the output file.
# 
# In short, it generates a compilable C file from a multi-file project.

import context
import sys

def show_project_info(ctx):
      print("====================== PROJECT INFO ======================")
      print("Project path: " + ctx.path)
      print("Entry point: " + ctx.entry_point)
      print("Output file: " + ctx.output_file)
      print("Total indexed files: " + str(len(ctx.indexed_files)))
      print("Project size: " + str(ctx.get_project_size()) + " bytes")
      print("C files: ")
      show_indexed_files(ctx.c_files)
      print("Header files: ")
      show_indexed_files(ctx.h_files)


def show_indexed_files(file_list):
      for file in file_list:
            print("     - " + file)

if __name__ == "__main__":
      # Check if the arguments are valid
      if len(sys.argv) != 5:
            print("Usage: python main.py <option> <path> <entry_point> <output_file>")
            exit(1)

      if sys.argv[1] == "-s":
            print("Building project context for single file project...")
            ctx = context.ProjectContext(sys.argv[2], sys.argv[3], sys.argv[4])
            ctx.index_project()
            show_project_info(ctx)
            ctx.write_output_file()

      elif sys.argv[1] == "-c":
            print("Indexing project for CodeBlocks...")
            ctx = context.CodeBlocksContextCreator(sys.argv[2], sys.argv[3], sys.argv[4])
            ctx.index_project()
            ctx.build_codeblocks_project()

      else:
            print("Invalid option " + sys.argv[1])


