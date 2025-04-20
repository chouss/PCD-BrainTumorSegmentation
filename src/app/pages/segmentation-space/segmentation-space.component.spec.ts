import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SegmentationSpaceComponent } from './segmentation-space.component';

describe('SegmentationSpaceComponent', () => {
  let component: SegmentationSpaceComponent;
  let fixture: ComponentFixture<SegmentationSpaceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SegmentationSpaceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SegmentationSpaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
