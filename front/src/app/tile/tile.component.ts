import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'tile',
  templateUrl: './tile.component.html',
  styleUrls: ['./tile.component.scss']
})
export class TileComponent implements OnInit {

  @Input() value: number
  @Input() type: string
  constructor() { }

  ngOnInit(): void {
  }

}
