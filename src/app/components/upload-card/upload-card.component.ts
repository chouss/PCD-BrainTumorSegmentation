import { Component,Input } from '@angular/core';
import { UploadService } from '../../services/pythonServices/upload.service';

@Component({
  selector: 'app-upload-card',
  imports: [],
  templateUrl: './upload-card.component.html',
  styleUrl: './upload-card.component.scss'
})
export class UploadCardComponent {
@Input ()
typeIMG:string='';
selectedFile: File | null = null;
uploadResponse: string = '';

constructor(private dataService: UploadService) {}

onFileSelected(event: Event) {
  const input = event.target as HTMLInputElement;
  if (input.files?.length) {
    this.selectedFile = input.files[0];
  }
  this.upload()
}

upload() {
  if (this.selectedFile) {
    this.dataService.uploadFile(this.selectedFile , this.typeIMG).subscribe({
      next: (res) => {
        this.uploadResponse = res.message;
      },
      error: (err) => {
        console.error(err);
        this.uploadResponse = 'Upload failed.';
      }
    });
  }
}

}
