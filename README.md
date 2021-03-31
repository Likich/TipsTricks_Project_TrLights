# TipsTricks-Project-TrLights
<br>
Article on databases: https://www.researchgate.net/publication/327808220_The_DriveU_Traffic_Light_Dataset_Introduction_and_Comparison_with_Existing_Datasets <br> <br>

## Results
Faster R-CNN FPN on Lisa dataset, 3 epochs, batch = 16, LR_on_plateau, Adam <br>
https://drive.google.com/file/d/1h7PfPPYH8ZyR1egjDF1vl0-83aseZHR-/view?usp=sharing <br>
Performance on test video: https://drive.google.com/file/d/1F-1yy4BSjNHT75andGyOidVUf_m__CGx/view?usp=sharing <br> <br>
Faster R-CNN on Lisa+Bosch datasets, 8k+8k photos, 3 epochs <br>
https://drive.google.com/file/d/1RiIs1-aqPIEr4a_EP64SnuQvvmZNubeP/view?usp=sharing <br>
Perfomance on test video: https://drive.google.com/file/d/12P5xmOzrwSSlhCHv7AHcfIB0U6CP6A11/view?usp=sharing <br><br>
8 epochs with Bosch, Lisa and S2TLD datasets <br>
https://drive.google.com/file/d/1zrfmFG5lz84of6Ul7e0USBSlIyzdm2ZX/view?usp=sharing <br> <br>
Detection at night <br>
https://drive.google.com/file/d/16lRq48L-5rzCxDWzMRgPQ5FR5rmwFm-4/view?usp=sharing


## Some info

We used Faster RCNN to find traffic lights on video. Training data consists of LISA, Bosch and S2TLD datasets. You can find links for this datasets in "useful links" file. <br><br>
Our task was finding traffic lights only at daytime thus we didn't use night data. Although you can find some expirements with night data in "Detection/" directory. <br><br>
Faster RCNN gives very good results in finding traffi lights but one main downside is speed. So, since Faster RCNN is not fast enough to find boxes for each frame, we processed only each 4-th frame. Results may not be as accurate but the speed significantly increases. Also there's no much need in finding accurate position of a traffic lights (as we only care if we can move or not at the moment) and the difference in update time for boxes almost can not be caught by a human eye (0.012 sec instead of 0.003 sec for a 30 fps video) <br><br> 
Every file with .py extension contains one cell from final .ipynb file.  You can find final .ipynb file in "/Detection" folder. ALso this folder contains some of our expirements.<br>
