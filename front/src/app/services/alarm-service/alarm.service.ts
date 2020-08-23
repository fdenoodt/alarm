import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'
import { HttpClient } from '@angular/common/http'
import { mergeMap } from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})
export class AlarmService {

  private url = "http://192.168.0.186:5000"

  constructor(private http: HttpClient) {
  }

  getServerTime(): Observable<{ hour, minute }> {
    return this.http.get<{ hour, minute }>(`${this.url}/time`)
  }

  getTime(): Observable<{ hour, minute }> {
    return this.http.get<{ hour, minute }>(this.url)
  }

  difference(serverTime: { hour, minute }): { hour, minute } {
    const serverHour = serverTime.hour
    const serverMinute = serverTime.minute

    const d = new Date();
    const currH = d.getHours();
    const currM = d.getMinutes();

    const diffH = serverHour - currH
    const diffM = serverMinute - currM

    return { hour: diffH, minute: diffM }
  }

  setTime(time: { hour, minute }): Observable<any> {

    return this.getServerTime().pipe(
      mergeMap((serverTime: { hour, minute }) => {
        const difference = this.difference(serverTime)
        let hour = time.hour + difference.hour
        let minute = time.minute + difference.minute

        console.log(difference);
        console.log(hour);
        console.log(minute);


        if (hour > 23)
          hour = hour - 24
        if (minute > 59)
          minute = minute - 60

        if (hour < 0)
          hour = hour + 24
        if (minute < 0)
          minute = minute + 60

        const formData = new FormData();
        formData.append('hour', hour);
        formData.append('minute', minute);

        return this.http.post<{ hour, minute }>(this.url, formData)
      })
    )



  }

}
