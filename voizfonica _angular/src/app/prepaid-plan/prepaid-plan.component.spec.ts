import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrepaidPlanComponent } from './prepaid-plan.component';

describe('PrepaidPlanComponent', () => {
  let component: PrepaidPlanComponent;
  let fixture: ComponentFixture<PrepaidPlanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PrepaidPlanComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PrepaidPlanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
