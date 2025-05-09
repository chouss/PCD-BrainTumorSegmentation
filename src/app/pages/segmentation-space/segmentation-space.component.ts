import { Component } from '@angular/core';
import { UploadCardComponent } from "../../components/upload-card/upload-card.component";
import { SegmentationButtonComponent } from "../../components/segmentation-button/segmentation-button.component";
import { GenerateSliceComponent } from "../../components/generate-slice/generate-slice.component";

@Component({
  selector: 'app-segmentation-space',
  imports: [UploadCardComponent, SegmentationButtonComponent, GenerateSliceComponent],
  templateUrl: './segmentation-space.component.html',
  styleUrl: './segmentation-space.component.scss'
})
export class SegmentationSpaceComponent {

}
