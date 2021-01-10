import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ScanService } from '../../services/scan.service';

@Component({
  selector: 'app-scan-form',
  templateUrl: './scan-form.component.html',
  styleUrls: ['./scan-form.component.scss'],
})
export class ScanFormComponent implements OnInit {
  host: string = '';
  @Output() newScanCreated = new EventEmitter<string>();

  constructor(private scanService: ScanService, private router: Router) {}

  createScan(event: Event): void {
    event.preventDefault();
    this.scanService.createScan(this.host).subscribe((scan) => {
      this.router.navigate(['/nmap', scan.uuid]);
    });
  }

  ngOnInit(): void {}
}
