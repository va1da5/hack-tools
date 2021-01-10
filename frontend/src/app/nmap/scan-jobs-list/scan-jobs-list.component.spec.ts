import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ScanJobsListComponent } from './scan-jobs-list.component';

describe('ScanJobsListComponent', () => {
  let component: ScanJobsListComponent;
  let fixture: ComponentFixture<ScanJobsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ScanJobsListComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ScanJobsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
