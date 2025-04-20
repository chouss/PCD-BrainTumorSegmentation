import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SegmentationButtonComponent } from './segmentation-button.component';

describe('SegmentationButtonComponent', () => {
  let component: SegmentationButtonComponent;
  let fixture: ComponentFixture<SegmentationButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SegmentationButtonComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SegmentationButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
