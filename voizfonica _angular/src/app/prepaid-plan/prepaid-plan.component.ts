import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-prepaid-plan',
  templateUrl: './prepaid-plan.component.html',
  styleUrls: ['./prepaid-plan.component.css']
})
export class PrepaidPlanComponent implements OnInit {

    items:any;
    error:any;
  constructor(private api: ApiService) { }

  ngOnInit(): void {
  this.get();
  }
  get=()=> {
    this.api.getItems().subscribe(
    data=>{ this.items=data;},
     );
         (error: any) => this.error = error
  }


}
