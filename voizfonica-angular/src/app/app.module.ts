// import { NgModule } from '@angular/core';
// import { BrowserModule } from '@angular/platform-browser';
//
// import { AppRoutingModule } from './app-routing.module';
// import { AppComponent } from './app.component';
//
// @NgModule({
//   declarations: [
//     AppComponent
//   ],
//   imports: [
//     BrowserModule,
//     AppRoutingModule
//   ],
//   providers: [],
//   bootstrap: [AppComponent]
// })
// export class AppModule { }
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { ApiService } from './api.service';
import { AppComponent } from './app.component';
import { PrepaidPlanComponent } from './prepaid-plan/prepaid-plan.component';
import { AppRoutingModule, ArrayOfComponents } from './app-routing.module';
import { PostpaidRechargeComponent } from './postpaid-recharge/postpaid-recharge.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { BuyComponent } from './buy/buy.component';
import { DonglePlanComponent } from './dongle-plan/dongle-plan.component';
import { RechargeComponent } from './recharge/recharge.component';
import { QueryComponent } from './query/query.component';
import { PortComponent } from './port/port.component';





@NgModule({
  declarations: [
    AppComponent,
    PrepaidPlanComponent,
    ArrayOfComponents,
    PostpaidRechargeComponent,
    DonglePlanComponent,
    BuyComponent,
    DonglePlanComponent,
    RechargeComponent,
    QueryComponent,
    PortComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [
    ApiService,
  ],
  bootstrap: [
    AppComponent,
  ],
})
export class AppModule { }
