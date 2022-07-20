import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable(
{ providedIn:'root'
})
export class ApiService {

  api_link:string='http://localhost:8000/';

  constructor(private http: HttpClient) { }

//READ
  getItems() {

    return this.http.get(this.api_link + 'api/list1/');
  }

  getpostpaidItems() {

    return this.http.get(this.api_link + 'api/list2/');
  }

  getdongleItems() {

    return this.http.get(this.api_link + 'api/list3/');
  }

  customerdata(data:any)
  {
    return this.http.post(this.api_link+'api/list4/',data)
  }

  paymentdata(data:any)
  {
    return this.http.post(this.api_link+'api/list6/',data)
  }

  querydata(data:any)
  {
    return this.http.post(this.api_link+'api/list7/',data)
  }

  getvalues (data:any)
  {
    return this.http.post(this.api_link+'api/list4/',data)
  }

  //UPDATE
  //DELETE
  //CREATE
}

