import { Component, OnInit } from '@angular/core';
import { AlarmService } from './services/alarm-service/alarm.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  minutes: number[] = []
  hours: number[] = []
  pm: boolean

  selectedHour: number = 9
  selectedMinute: number = 0

  constructor(private alarmService: AlarmService) {
    // Set up hour options
    for (let i = 0; i < 12; i++) {
      this.minutes.push(i * 5)
      this.hours.push(i + 1)
    }
  }

  ngOnInit() {
    this.alarmService.getTime().subscribe(
      time => {
        this.selectedHour = time.hour ?? 0
        this.selectedMinute = time.minute ?? 0
      },
      err => alert("Error")
    )
  }

  setTime() {
    this.alarmService.setTime({ hour: this.selectedHour, minute: this.selectedMinute }).subscribe(
      _ => { },
      err => alert("Error"))
  }

  stateChanged(isActive) {
    this.pm = isActive
    this.selectedHour = this.adaptToPM(this.pm, this.selectedHour)
    this.setTime()
  }

  timeSelected(data: { number, type }) {
    let number: number = parseInt(data.number)
    const type = data.type

    if (type == 'hour')
      number = this.adaptToPM(this.pm, number)

    type == 'hour' ? this.selectedHour = number : this.selectedMinute = number
    this.setTime()
  }

  adaptToPM(isPM: boolean, selectedHour: number): number {
    let hour = selectedHour

    if (isPM) {
      if (hour < 12) {
        hour += 12
      }
      else if (hour == 12) {
        hour = 0
      }

    } else {
      if (hour > 12)
        hour -= 12
      else if (hour == 0)
        hour = 12
    }

    return hour
  }


}
