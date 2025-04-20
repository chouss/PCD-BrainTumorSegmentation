import nnunetv2,os,subprocess,sys

def segmentationFN():
    id=0
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'nnUnet'))
    os.environ['nnUNet_results'] = base_dir
    input_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pythonFiles','uploads',str(id)))
    output_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pythonFiles','outputs'))

    command = [
    "nnUNetv2_predict",
    "-i", str(input_folder),
    "-o", str(output_folder),
    "-d", "220",
    "-tr", "nnUNetTrainer_250epochs",
    "-c", "3d_fullres",
    "-f", "0"
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    segmentationIsDone=False
    # Print output live
    for line in process.stdout:
        print(line, end="")
        if line[0:4]=="done":
            segmentationIsDone = True

    process.wait()
    return (segmentationIsDone)




