import { Component, Input  } from '@angular/core';

@Component({
  selector: 'app-profil-card',
  imports: [],
  templateUrl: './profil-card.component.html',
  styleUrl: './profil-card.component.scss'
})
export class ProfilCardComponent {
  @Input() pName: string = '';
  @Input() imgURL: string = '';
  @Input() linkdinURL: string = '';


}
