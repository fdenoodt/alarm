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

    if (this.pm && this.selectedHour)
      this.selectedHour += 12
    else
      this.selectedHour -= 12

  }

  timeSelected(data: { number, type }) {
    let number: number = parseInt(data.number)
    const type = data.type

    if (this.pm && type == 'hour')
      number += 12

    type == 'hour' ? this.selectedHour = number : this.selectedMinute = number
  }


}
