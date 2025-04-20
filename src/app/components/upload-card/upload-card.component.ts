import { Component,Input } from '@angular/core';

@Component({
  selector: 'app-upload-card',
  imports: [],
  templateUrl: './upload-card.component.html',
  styleUrl: './upload-card.component.scss'
})
export class UploadCardComponent {
@Input ()
typeIMG:string='';
}
