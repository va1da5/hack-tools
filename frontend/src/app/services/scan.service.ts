import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Scan } from '../models/scan.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ScanService {
  constructor(private http: HttpClient) {}

  apiHost: string = environment.apiHost;

  getScanJobs(): Observable<Scan[]> {
    return this.http.get<Scan[]>(`${this.apiHost}/api/scan/`);
  }

  getScanDetails(uuid: string): Observable<Scan> {
    return this.http.get<Scan>(`${this.apiHost}/api/scan/${uuid}/`);
  }

  getScanResults(uuid: string): Observable<string> {
    return this.http.get<string>(`${this.apiHost}/api/scan/${uuid}/result/`);
  }

  createScan(host: string): Observable<Scan> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
    };
    const postData = { host };
    return this.http.post<Scan>(
      `${this.apiHost}/api/scan/`,
      postData,
      httpOptions
    );
  }
}
