import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'toggle',
  templateUrl: './toggle.component.html',
  styleUrls: ['./toggle.component.scss']
})
export class ToggleComponent implements OnInit {

  constructor() { }

  active: boolean = false

  ngOnInit(): void {

  }

}
