import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { Scan } from '../../models/scan.model';

@Component({
  selector: 'app-scan-timeline',
  templateUrl: './scan-timeline.component.html',
  styleUrls: ['./scan-timeline.component.scss'],
})
export class ScanTimelineComponent implements OnInit {
  @Input() scan: Scan = new Scan();
  @Output() cancelScan = new EventEmitter<boolean>();

  constructor() {}

  get isScanFinished(): boolean {
    return ['SUCCESS', 'FAILURE', 'REVOKED'].includes(this.scan.state);
  }

  get wasScanSuccessful(): boolean {
    return this.scan.state == 'SUCCESS';
  }

  ngOnInit(): void {}
}
