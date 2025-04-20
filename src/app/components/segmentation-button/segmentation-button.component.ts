import { Component } from '@angular/core';
import { UploadService } from '../../services/pythonServices/upload.service';

@Component({
  selector: 'app-segmentation-button',
  imports: [],
  templateUrl: './segmentation-button.component.html',
  styleUrl: './segmentation-button.component.scss'
})
export class SegmentationButtonComponent {
  constructor(private dataService: UploadService) {}
  
  uploadResponse: string = 'Nothing yet';

  DoSegmentation() {
    this.dataService.startSegmentation().subscribe({
      next: (res) => {
        this.uploadResponse = res.message;
      },
      error: (err) => {
        console.error(err);
        this.uploadResponse = 'Segmentation failed.';
      }
    });
  }
}
