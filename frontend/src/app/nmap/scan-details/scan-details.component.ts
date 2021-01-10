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

  getResults(): void {
    this.scanService.getScanResults(this.scanUuid).subscribe((scanResult) => {
      this.scanResult = scanResult;
    });
  }

  getScan(): void {
    this.scanService.getScanDetails(this.scanUuid).subscribe((scan) => {
      this.scan = scan;
    });
  }

  monitorScan(): void {
    // TODO: This needs to be reviewed and likely replaced with components from RxJs
    this.getScan();
    this.getResults();
    const monitorInterval = setInterval(() => {
      if (['SUCCESS', 'FAILURE', 'REVOKED'].includes(this.scan.state)) {
        clearInterval(monitorInterval);
        this.getResults();
      }
      this.getScan();
    }, 1000);
  }

  ngOnInit(): void {
    this.activatedRoute.params.subscribe((params: Params) => {
      this.scanUuid = params.uuid;
      this.monitorScan();
    });
  }
}
