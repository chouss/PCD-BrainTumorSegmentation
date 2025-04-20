import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenerateSliceComponent } from './generate-slice.component';

describe('GenerateSliceComponent', () => {
  let component: GenerateSliceComponent;
  let fixture: ComponentFixture<GenerateSliceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GenerateSliceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GenerateSliceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
