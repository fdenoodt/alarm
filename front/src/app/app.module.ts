import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { TileComponent } from './tile/tile.component';
import { ToggleComponent } from './toggle/toggle.component';
import { AlarmService } from './services/alarm-service/alarm.service'
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    TileComponent,
    ToggleComponent
  ],
  imports: [
    BrowserModule,
    FlexLayoutModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [AlarmService],
  bootstrap: [AppComponent]
})
export class AppModule { }
