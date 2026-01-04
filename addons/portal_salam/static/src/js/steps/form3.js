// Define ClientsTable Component
class Form3 extends Component {
  static props = ['state', 'data']
  static components = {
    SituationIndex,
    SuppliersIndex,
    ClientsIndex,
    CompaniesIndex,
  }

  static template = xml`
    <div>
        <h5 for="situations" style="font-size: 16px; font-weight:bold; color: #F2643B;">
        التقويم البنكي للآخرين
        </h5>

        <div class="text-end mb-3">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                    data-bs-target="#createSituationModal">اضف طلب
            </button>
        </div>
        <SituationIndex state="props.state" />

        <h5 for="fournisseurs" style="font-size: 16px; font-weight:bold; color: #F2643B;">
            الموردون
        </h5>
        <div class="text-end mb-3">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                    data-bs-target="#createSupplierModal">اضف مورد
            </button>
        </div>
        <SuppliersIndex state="props.state" />

    
        <h5 for="clients" style="font-size: 16px; font-weight:bold; color: #F2643B;">
            الزبائن
        </h5>
        <div class="text-end mb-3">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                    data-bs-target="#createClientModal">اضف زبون
            </button>
        </div>
        <ClientsIndex state="props.state" />

        <h5 for="companies" style="font-size: 16px; font-weight:bold; color: #F2643B;">
            معلومات حول الشركات ذات الصلة (KDA)
        </h5>
        <div class="text-end mb-3">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                    data-bs-target="#createCompaniesModal">اضف شركة
            </button>
        </div>
        <CompaniesIndex state="props.state" />
        </div>
    `
}
