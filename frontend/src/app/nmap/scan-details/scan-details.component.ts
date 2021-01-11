import { Component, OnInit, Input, SimpleChange } from '@angular/core';
import { ScanService } from '../../services/scan.service';
import { Scan } from '../../models/scan.model';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-scan-details',
  templateUrl: './scan-details.component.html',
  styleUrls: ['./scan-details.component.scss'],
})
export class ScanDetailsComponent implements OnInit {
  scanUuid: string = '';
  scan: Scan = new Scan();
  scanResult: string = '';

  constructor(
    private scanService: ScanService,
    private activatedRoute: ActivatedRoute
  ) {}

  getResults(scanUuid: string): void {
    this.scanService.getScanResults(scanUuid).subscribe((scanResult) => {
      this.scanResult = scanResult;
    });
  }

  getScan(scanUuid: string): void {
    this.scanService.getScanDetails(scanUuid).subscribe((scan) => {
      this.scan = scan;
    });
  }

  // TODO: Review and update whole functionality because
  // of jittery user interaction with this component
  monitorScan(scanUuid: string): void {
    this.getScan(scanUuid);
    this.getResults(scanUuid);
    const monitorInterval = setInterval(() => {
      if (['SUCCESS', 'FAILURE', 'REVOKED'].includes(this.scan.state)) {
        clearInterval(monitorInterval);
        this.getResults(scanUuid);
      }
      this.getScan(scanUuid);
    }, 2000);
  }

  cancelScan(): void {
    this.scanService.cancelScan(this.scanUuid).subscribe((scan) => {
      this.scan = scan;
    });
  }

  ngOnInit(): void {
    this.activatedRoute.params.subscribe((params: Params) => {
      this.scanResult = '';
      this.scanUuid = params.uuid;
      this.monitorScan(this.scanUuid);
    });
  }
}
