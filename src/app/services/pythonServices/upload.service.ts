import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class UploadService {

  constructor(private http: HttpClient) {}

  uploadFile(file: File, type:string) {
    const formData = new FormData();
    formData.append('file', file);

    return this.http.post<{ message: string }>(
      `http://localhost:5000/uploadIMG?type=${type}`,
      formData
    );
    
  }
  startSegmentation() {
    return this.http.post<{ message: string }>('http://localhost:5000/start-segmentation', {});
  }

  getSegmentationImage(sliceIndex: number, orientation: string = 'axial') {
    const url = `http://localhost:5000/visualize-segmentation?slice_index=${sliceIndex}&orientation=${orientation}`;
    return this.http.get(url, { responseType: 'blob' });
  }
  

}
