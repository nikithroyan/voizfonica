import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrepaidPlanComponent } from './prepaid-plan/prepaid-plan.component'
import { PostpaidRechargeComponent } from './postpaid-recharge/postpaid-recharge.component'
import { BuyComponent } from './buy/buy.component'
import { DonglePlanComponent } from './dongle-plan/dongle-plan.component'
import { RechargeComponent } from './recharge/recharge.component'
import { QueryComponent } from './query/query.component'
import { PortComponent } from './port/port.component'


const routes: Routes = [
  {path:'prepaid-plan', component:PrepaidPlanComponent},
  {path:'postpaid-plan', component:PostpaidRechargeComponent},
  {path:'buy', component:BuyComponent},
  {path:'dongle-plan', component:DonglePlanComponent},
  {path:'recharge', component:RechargeComponent},
  {path:'query', component:QueryComponent},
  {path:'port', component:PortComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const ArrayOfComponents = [PrepaidPlanComponent, PostpaidRechargeComponent,
 BuyComponent, DonglePlanComponent, RechargeComponent,QueryComponent, PortComponent]
