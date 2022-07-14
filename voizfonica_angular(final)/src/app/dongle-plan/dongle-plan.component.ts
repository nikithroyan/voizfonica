import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-dongle-plan',
  templateUrl: './dongle-plan.component.html',
  styleUrls: ['./dongle-plan.component.css']
})
export class DonglePlanComponent implements OnInit {

    items:any;
    error:any;
  constructor(private api: ApiService) { }

  ngOnInit(): void {
  this.get();
  }
  get=()=> {
    this.api.getdongleItems().subscribe(
    data=>{ this.items=data;},
     );
         (error: any) => this.error = error
  }


}
