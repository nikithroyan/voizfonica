import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DonglePlanComponent } from './dongle-plan.component';

describe('DonglePlanComponent', () => {
  let component: DonglePlanComponent;
  let fixture: ComponentFixture<DonglePlanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DonglePlanComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DonglePlanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
