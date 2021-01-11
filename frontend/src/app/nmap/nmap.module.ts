import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { ClarityModule } from '@clr/angular';

import { NmapViewComponent } from './nmap-view/nmap-view.component';
import { ScanJobsListComponent } from './scan-jobs-list/scan-jobs-list.component';
import { ScanFormComponent } from './scan-form/scan-form.component';
import { ScanDetailsComponent } from './scan-details/scan-details.component';
import { ScanTimelineComponent } from './scan-timeline/scan-timeline.component';

const routes: Routes = [
  {
    path: 'nmap',
    component: NmapViewComponent,
    children: [
      {
        path: 'new',
        component: ScanFormComponent,
      },
      {
        path: '',
        component: ScanFormComponent,
      },
      {
        path: ':uuid',
        component: ScanDetailsComponent,
      },
    ],
  },
];

@NgModule({
  imports: [
    FormsModule,
    ClarityModule,
    CommonModule,
    RouterModule.forChild(routes),
  ],
  declarations: [
    NmapViewComponent,
    ScanJobsListComponent,
    ScanFormComponent,
    ScanDetailsComponent,
    ScanTimelineComponent,
  ],
  exports: [RouterModule],
})
export class NmapModule {}
