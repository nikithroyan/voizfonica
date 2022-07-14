import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-postpaid-recharge',
  templateUrl: './postpaid-recharge.component.html',
  providers : [ApiService],
  styleUrls: ['./postpaid-recharge.component.css']
})
export class PostpaidRechargeComponent implements OnInit {

    items:any;
    error:any;
  constructor(private api: ApiService) { }

  ngOnInit(): void {
  this.get();
  }
  get=()=> {
    this.api.getpostpaidItems().subscribe(
    data=>{ this.items=data;},
     );
         (error: any) => this.error = error
  }


}
