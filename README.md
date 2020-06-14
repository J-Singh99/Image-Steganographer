Welcome to the #Steganographer!

This application's sole purpose is to guard one's privacy over the internet (and real life)
while doing something as simple as sharing a file. 

The idea is to take any file type and hide it in another file type.

This Steganographer offers the ability to hide Image and Text inside another image.
More can be found about this in the 'Write Up.odt' file which explains the vision, the concept
and the scope of this project, along with it's benefits and shortcomings. 

**** NOTE ****
This folder includes the Command Line Interface Version of the project.
The complete project along with the frontend and database handling has been uploaded to Github (due to space constraints
link: https://github.com/J-Singh99/Image-Steganographer.git)
**************

-> HOW TO USE (HIDE)
  1. Keep ready a suitable image (size greater than 50KB works best!) in the same file as the project.
  2. If you want to hide text, you can directly enter it into the program. 
      For larger texts, the command 'cat filename.txt' should work (for LINUX/MAC).
  3. If you want to hide an image, chose a much smaller sized image.
  4. Run Hide.py (through the command line). Thats it!! 
  5. The CLI is all set to help you out.

-> HOW TO USE (REVEAL)
  1. Assuming you have an image with some hidden information, keep the image ready in the same file.
  2. Run Reveal.py (through the command line). Thats it!!!
  3. The CLI is all set to help you out.
  
-> MORE HELP
  In case the above instructions are not clear, just run the 'python3 Hide/Reveal.py -h' on the shell.
  Both the scripts will display the help text which will get you on your way to Hiding and Revealing.

-> REQUIREMENTS
  numpy (pip install numpy)
  argparse (pip install argparse)
  cv2 (pip install opencv-python)
  
-> MORE INFORMATION
  In case of any queries, please feel free to contact:
  
  Jaspreet Singh (18103107)
  jaspreet099@gmail.com
  8800112953
  
  
