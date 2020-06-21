import { Component, OnInit } from '@angular/core';

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

  constructor() {
    // Set up hour options
    for (let i = 0; i < 12; i++) {
      this.minutes.push(i * 5)
      this.hours.push(i + 1)
    }
  }

  stateChanged(isActive) {
    this.pm = isActive

    this.selectedHour = this.adaptToPM(this.pm, this.selectedHour)
  }

  timeSelected(data: { number, type }) {
    let number: number = parseInt(data.number)
    const type = data.type

    if (type == 'hour')
      number = this.adaptToPM(this.pm, number)

    type == 'hour' ? this.selectedHour = number : this.selectedMinute = number
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
