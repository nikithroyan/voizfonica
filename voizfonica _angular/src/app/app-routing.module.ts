import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PrepaidPlanComponent } from './prepaid-plan/prepaid-plan.component'

const routes: Routes = [
  {
    path:'prepaid-plan', component:PrepaidPlanComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const ArrayOfComponents = [PrepaidPlanComponent]
