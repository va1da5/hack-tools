import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ScanTimelineComponent } from './scan-timeline.component';

describe('ScanTimelineComponent', () => {
  let component: ScanTimelineComponent;
  let fixture: ComponentFixture<ScanTimelineComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ScanTimelineComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ScanTimelineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
