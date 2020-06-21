import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'tile',
  templateUrl: './tile.component.html',
  styleUrls: ['./tile.component.scss']
})
export class TileComponent implements OnInit {

  @Input() value: number
  @Input() type: string
  @Output() onClick: EventEmitter<{ number, type }> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  select() {
    this.onClick.emit({ number: this.value, type: this.type });
  }

}
