import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NmapViewComponent } from './nmap-view.component';

describe('NmapViewComponent', () => {
  let component: NmapViewComponent;
  let fixture: ComponentFixture<NmapViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NmapViewComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NmapViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
