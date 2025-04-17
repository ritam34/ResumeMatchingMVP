import os
import logging, time

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

li = os.listdir('/Volumes/Seagate Expansion Drive/skybits dataset/stackexchange1')

comm = "7z x -y stackexchange/"

for i in range(1, len(li)):
	name = li[i]
	print("[INFO: EXTRACTION OF FILE", i, "-", name, "UNDER PROGRESS]")

	newname = li[i][:-3]
	os.system("mkdir "+ newname)
	commTemp = comm + name + " -o" + newname
	os.system("cd "+ newname)
	os.system(commTemp)
	os.system("cd ..")
	print("")

print("EVERYTHING OK, SUCCESSFULLY EXTRACTED ALL THE FILES!")


# updated code
# import os
# import subprocess
# import logging

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# input_dir = "/Volumes/Seagate Expansion Drive/skybits dataset/stackexchange1"
# output_base = "/Volumes/Seagate Expansion Drive/skybits dataset/stackexchange_extracted"

# os.makedirs(output_base, exist_ok=True)

# files = [f for f in os.listdir(input_dir) if f.endswith(".7z")]

# for i, filename in enumerate(files, 1):
#     name = filename[:-3]  # Strip '.7z'
#     input_path = os.path.join(input_dir, filename)
#     output_path = os.path.join(output_base, name)
#     os.makedirs(output_path, exist_ok=True)

#     logging.info(f"Extracting file {i} - {filename} to {output_path}")

#     try:
#         subprocess.run(["7z", "x", "-y", input_path, f"-o{output_path}"], check=True)
#     except subprocess.CalledProcessError as e:
#         logging.error(f"Extraction failed for {filename}: {e}")

# logging.info("✅ All files extracted successfully.")
