import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { UploadService } from '../../services/pythonServices/upload.service';
import { NgIf } from '@angular/common';
@Component({
  selector: 'app-generate-slice',
  imports: [FormsModule,NgIf],
  templateUrl: './generate-slice.component.html',
  styleUrl: './generate-slice.component.scss'
})
export class GenerateSliceComponent {
  public selectedSlice : number =70 ;
  public orientation : string = 'axial';
  segmentationImgUrl: string | null = null;

  constructor(private dataService: UploadService) {}

  
  DoVisualizeSlice() {
    this.dataService.getSegmentationImage(this.selectedSlice, this.orientation).subscribe({
      next: (blob) => {
        const url = URL.createObjectURL(blob);
        this.segmentationImgUrl = url;
      },
      error: (err) => {
        console.error(err);
      }
    });
  }
}
