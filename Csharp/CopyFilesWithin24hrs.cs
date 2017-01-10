using System;
using System.IO;

namespace ConsoleApplication12
{
    class Program
    {


        public static void copyFiles(string sourceFolder, string destinationFolder)
        {

            //checks destination folder path to confirm it exits. If not folder is created.
            if (!Directory.Exists(destinationFolder));
            {
                Directory.CreateDirectory(destinationFolder);

            }

                //Shows the  time 24 hrs ago in the console. 
                Console.WriteLine("{0}  files created after this time will be copied.", DateTime.Now.AddDays(-1));

                //uses the EnumerateFiles static method.. 
                //Another possible option is GetFiles static mehod. 
                //EnumerateFiles can be more efficient if there is a large number of file to be copied.
                foreach (var file in Directory.EnumerateFiles(sourceFolder))
                {

                    DateTime fileLastWriteTime = File.GetLastWriteTime(file);
                    DateTime fileCreationTime = File.GetCreationTime(file);

                    if (fileLastWriteTime > DateTime.Now.AddDays(-1))
                    {
                        if (fileCreationTime > DateTime.Now.AddDays(-1))
                        {
                            File.Copy(file, file.Replace(sourceFolder, destinationFolder), true);

                        }
                        //Copies the file from the source folder to destination folder. If the file already exists, the latest version overwrites the older version.
                        File.Copy(file, file.Replace(sourceFolder, destinationFolder), true);

                        Console.WriteLine("{0} file has been copied", file);
                    }
                }

                Console.WriteLine("File copying is completed");
            }
       


        static void Main(string[] args)

        {
                //Add source and destination path strings.  Strings and method call comment marks can be removed to run code.
                //string source = @"";
                //string destination = @"";

                //copyFiles(source, destination);
            
        }
    }

}