import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  minutes = []
  hours = []

  constructor() {

    // Set up hour options
    for (let i = 0; i < 12; i++) {
      this.minutes.push(i * 5)
      this.hours.push(i + 1)
    }
  }

}
