import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { TileComponent } from './tile/tile.component';

@NgModule({
  declarations: [
    AppComponent,
    TileComponent
  ],
  imports: [
    BrowserModule,
    FlexLayoutModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
