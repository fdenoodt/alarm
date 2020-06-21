import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AlarmService {

  private url = "http://192.168.0.186:5000"

  constructor(private http: HttpClient) {
  }

  getTime(): Observable<{ hour, minute }> {
    return this.http.get<{ hour, minute }>(this.url)
  }

  setTime(time: { hour, minute }): Observable<any> {
    const formData = new FormData();
    formData.append('hour', time.hour);
    formData.append('minute', time.minute);
    return this.http.post<{ hour, minute }>(this.url, formData)
  }

}
