import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Scan } from '../../models/scan.model';
import { trigger, transition, useAnimation } from '@angular/animations';
import { pulse } from 'ng-animate';
import { ScanService } from '../../services/scan.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-scan-jobs-list',
  templateUrl: './scan-jobs-list.component.html',
  styleUrls: ['./scan-jobs-list.component.scss'],
  animations: [trigger('pulse', [transition('* => *', useAnimation(pulse))])],
})
export class ScanJobsListComponent implements OnInit {
  pulse: any;

  @Input() selectedScanId: string = '';

  scans: Scan[] = [];

  constructor(private scanService: ScanService, private router: Router) {}

  getScans(): void {
    this.scanService.getScanJobs().subscribe((scans) => {
      this.scans = scans;
    });
  }

  ngOnInit(): void {
    this.getScans();
    setInterval(this.getScans.bind(this), 5000);
  }
}
