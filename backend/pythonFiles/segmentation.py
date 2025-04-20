import nnunetv2,os,subprocess

def segmentation():

    os.environ['nnUNet_results'] = r'C:\Users\oussa\OneDrive\Documents\Angular\nnunet\nnUNet_results'
    command = [
    "nnUNetv2_predict",
    "-i", r"C:\Users\oussa\OneDrive\Documents\Angular\nnunet\niiImages",
    "-o", r"C:\Users\oussa\OneDrive\Documents\Angular\nnunet\outputImages",
    "-d", "220",
    "-tr", "nnUNetTrainer_250epochs",
    "-c", "3d_fullres",
    "-f", "0"
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Print output live
    for line in process.stdout:
        print(line, end="")

    process.wait()
    
segmentation()
