import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'toggle',
  templateUrl: './toggle.component.html',
  styleUrls: ['./toggle.component.scss']
})
export class ToggleComponent implements OnInit {

  @Output() stateChange: EventEmitter<boolean> = new EventEmitter();
  constructor() { }
  active: boolean = false

  ngOnInit(): void {

  }

  toggleVisibility() {
    this.stateChange.emit(this.active);
  }

}
